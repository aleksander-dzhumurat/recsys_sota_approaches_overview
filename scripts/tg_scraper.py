"""
Telegram channel scraper.

Scrapes messages from public Telegram channels using the Telegram API.
Requires API credentials from https://my.telegram.org/apps.

Usage:
    uv run scripts/tg_scraper.py
    uv run scripts/tg_scraper.py --channel my_channel
    uv run scripts/tg_scraper.py --channel my_channel --limit 100 --output output.json
"""

import argparse
import asyncio
import json
import os
from datetime import datetime

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError


def load_credentials() -> tuple[str, str]:
    """Load Telegram API credentials from .env file."""
    load_dotenv()

    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")

    if not api_id or not api_hash:
        raise ValueError(
            "TELEGRAM_API_ID and TELEGRAM_API_HASH must be set in .env file. "
            "Get them from https://my.telegram.org/apps"
        )

    return api_id, api_hash


async def authenticate(api_id: str, api_hash: str, session_name: str) -> TelegramClient:
    """Authenticate with Telegram API, handling phone verification."""
    client = TelegramClient(session_name, int(api_id), api_hash)

    await client.start()

    if not await client.is_user_authorized():
        phone = os.getenv("TELEGRAM_PHONE")
        if not phone:
            phone = input("Enter your phone number (with country code): ")

        await client.send_code_request(phone)

        try:
            await client.sign_in(phone, input("Enter the code: "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input("Enter your 2FA password: "))

    return client


async def scrape_channel(
    client: TelegramClient, channel: str, limit: int | None = None
) -> list[dict]:
    """Scrape messages from a Telegram channel."""
    messages = []

    async for message in client.iter_messages(channel, limit=limit):
        msg_data = {
            "id": message.id,
            "date": message.date.isoformat() if message.date else None,
            "text": message.text,
            "sender_id": message.sender_id,
        }

        # Add media info if present
        if message.media:
            msg_data["has_media"] = True
            msg_data["media_type"] = type(message.media).__name__

        messages.append(msg_data)

    return messages


async def main():
    """Main entry point for the scraper."""
    parser = argparse.ArgumentParser(
        description="Scrape messages from Telegram channels"
    )
    parser.add_argument(
        "--channel", type=str, help="Channel username or link to scrape"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of messages to fetch (default: all)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.json",
        help="Output file path (default: output.json)",
    )

    args = parser.parse_args()

    if not args.channel:
        # Interactive mode - list available channels
        api_id, api_hash = load_credentials()
        session_name = os.getenv("SESSION_NAME", "my_session")

        client = await authenticate(api_id, api_hash, session_name)

        print("Available channels you have access to:")
        async for dialog in client.iter_dialogs():
            if dialog.is_channel and not dialog.is_group:
                print(f"  - {dialog.name} (@{dialog.entity.username})")

        await client.disconnect()
        return

    # Scrape the specified channel
    api_id, api_hash = load_credentials()
    session_name = os.getenv("SESSION_NAME", "my_session")

    print("Connecting to Telegram...")
    client = await authenticate(api_id, api_hash, session_name)

    print(f"Scraping channel: {args.channel}")
    messages = await scrape_channel(client, args.channel, args.limit)

    # Save to file
    output_data = {
        "channel": args.channel,
        "scraped_at": datetime.now().isoformat(),
        "message_count": len(messages),
        "messages": messages,
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(messages)} messages to {args.output}")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

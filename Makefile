CURRENT_DIR = $(shell pwd)
include .env
export

setup:
	mkdir -p data

setup:
	mkdir -p ${CURRENT_DIR}/.research_results/articles_pdf
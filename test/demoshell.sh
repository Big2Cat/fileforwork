#!/bin/bash
#/home/kong/.virtualenvs/Spider_py2/bin/activate Py3
#source ~/.bashrc
source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME=$HOME/.virtualenvs
workon Spider_py2
cd /home/kong/workspace/ScrapyProject/BussinessInfoupload/BussinessInfo/spiders
scrapy crawl rmfygg > /home/kong/workspace/test/log1.log


#!/bin/bash
#
# Set or replace the jarvis alias in bashrc

FILE=${BASH_ALIAS_FILE:-~/.bashrc}

set_jarvis_docker() {
    set_alias "docker run -it --rm -v $(pwd):/project -e OPENAI_API_KEY=${OPENAI_API_KEY} jarvis:latest bash -c 'jarvis'"
}

set_jarvis_python() {
    set_alias "python ${pwd}/src/main.py"
}

set_alias() {

    remove_alias

    COMMAND=$1

    echo "Adding jarvis alias to bashrc"

    echo "alias jarvis='${COMMAND}'" >> $FILE

}

remove_alias() {

    sed -i "/alias jarvis=.*/d" $FILE

}

if [ "$1" == 'python' ]; then
    set_jarvis_python
else
    set_jarvis_docker
fi


echo "Jarvis added as an alias, plz restart the terminal or source the ${FILE} file"

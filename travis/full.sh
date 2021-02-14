#!/bin/bash

set -e -x

# Fake out any Travis env. vars. needed.
if [[ "${GITHUB_ACTIONS_RUNS_ON}" == "macos-latest" ]]; then
  export TRAVIS_OS_NAME=osx
else
  export TRAVIS_OS_NAME=linux
fi

# Install `virtualenv` globally (multibuild expects this to be available but
# does not check or install)
python -m pip install --upgrade virtualenv
if [[ "${GITHUB_ACTIONS_RUNS_ON}" == "macos-latest" ]]; then
  export PATH="${PATH}:/Library/Frameworks/Python.framework/Versions/2.7/bin"
else
  export PATH="${PATH}:/home/runner/.local/bin"
fi

source multibuild/common_utils.sh
source multibuild/travis_steps.sh
before_install
clean_code ${REPO_DIR} ${BUILD_COMMIT}
build_wheel ${REPO_DIR} ${PLAT}
install_run ${PLAT}

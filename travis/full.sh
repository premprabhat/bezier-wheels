#!/bin/bash

set -e -x

source multibuild/common_utils.sh
source multibuild/travis_steps.sh
before_install
clean_code ${REPO_DIR} ${BUILD_COMMIT}
build_wheel ${REPO_DIR} ${PLAT}
install_run ${PLAT}

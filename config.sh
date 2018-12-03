# Define custom utilities
# Test for OSX with [ -n "$IS_OSX" ]

function pre_build {
    :
}

function pip_opts {
    # Extra options for pip
    echo "-v"
}

function run_tests {
    echo "Executing run_tests ..."
    echo "python --version:"
    python --version
    if [[ -n "${IS_OSX}" ]]; then
        BEZIER_TESTS=${TRAVIS_BUILD_DIR}/bezier/tests
    else
        # I.e. running on a Docker container
        BEZIER_TESTS=/io/bezier/tests
    fi
    pytest ${BEZIER_TESTS}
}

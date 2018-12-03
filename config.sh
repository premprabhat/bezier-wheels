# Define custom utilities
# Test for OSX with [ -n "$IS_OSX" ]

function pre_build {
    python --version
}

function run_tests {
    python --version
    echo "BEZIER_WHEEL: ${BEZIER_WHEEL}"
    if [[ -n "${IS_OSX}" ]]; then
        echo "BEZIER_TESTS: ${TRAVIS_BUILD_DIR}/bezier/tests"
    else
        # I.e. running on a Docker container
        echo "BEZIER_TESTS: /io/bezier/tests"
    fi
}

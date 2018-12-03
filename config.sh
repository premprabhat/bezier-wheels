# Define custom utilities
# Test for OSX with [ -n "$IS_OSX" ]

function pre_build {
    python --version
}

function run_tests {
    python --version
    pytest ${TRAVIS_BUILD_DIR}/bezier/tests
}

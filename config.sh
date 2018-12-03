# Define custom utilities
# Test for OSX with [ -n "$IS_OSX" ]

function pre_build {
    python --version
}

function run_tests {
    python --version
    pytest bezier/tests
}

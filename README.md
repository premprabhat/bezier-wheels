# `bezier-wheels`

[![AppVeyor Build Status](https://img.shields.io/appveyor/ci/dhermes/bezier-wheels/master.svg?maxAge=3600&logo=appveyor&label=AppVeyor)](https://ci.appveyor.com/project/dhermes/bezier-wheels)
[![Travis CI Build Status](https://img.shields.io/travis/dhermes/bezier-wheels/master.svg?maxAge=3600&logo=travis&label=Travis%20CI)](https://travis-ci.org/dhermes/bezier-wheels)

Wheel Builder for [`bezier`][1]. This uses [`multibuild`][2] to
create wheels for

- `manylinux` (on Travis CI)
- macOS (on Travis CI)
- Windows (on AppVeyor)

and uploads the built wheels to a Google Cloud Storage (GCS) bucket specified
in the Travis CI and AppVeyor configurations. The service account credentials
authorized to upload the wheels to the bucket is encrypted in a platform
specific way as `travis/key.json.enc` and `appveyor/key.json.enc`.

## Travis CI

There are four encrypted environment variables, all of which are used for
the upload to GCS

- `encrypted_02a99c88fc32_iv`: OpenSSL initialization vector (`-iv`) for
  decrypting `travis/key.json.enc`.
- `encrypted_02a99c88fc32_key`: OpenSSL raw hex key (`-K`) for decrypting
  `travis/key.json.enc`.
- `GCS_BUCKET`: The name of the GCS bucket.
- `GOOGLE_CLOUD_PROJECT`: The project that owns the GCS bucket.

These are set in the [Travis CI settings][3] rather than as [`secure:`][4]
variables in `.travis.yml`.

## AppVeyor

There are three encrypted environment variables, all of which are used for
the upload to GCS

- `DECRYPT_KEY_JSON`: The `-secret` to pass to `appveyor-tools/secure-file`
  for decrypting `appveyor/key.json.enc`.
- `GCS_BUCKET`: The name of the GCS bucket.
- `GOOGLE_CLOUD_PROJECT`: The project that owns the GCS bucket.

These are set directly in `.appveyor.yml` as [`secure:`][5] variables
(encrypted in the [web UI][6]).

## GCS Upload

Rather than downloading the entire [`gcloud` SDK][7] a bare [`gsutil`][8]
install is used. Luckily this can be installed directly from [PyPI][9]
into a Python 2.7 (virtual) environment.

Since `gcloud` isn't available for authentication and since user interaction
isn't possible on CI platforms, a `.boto` configuration file is used and
a custom `BOTO_PATH` points to `{BEZIER_WHEELS_DIR}/.boto`. The script
`populate_boto.py` creates this `.boto` file and populates it with the path to
the decrypted service account credentials (`key.json`) as well as the default
Google Cloud project ID.

[1]: https://github.com/dhermes/bezier
[2]: https://github.com/matthew-brett/multibuild
[3]: https://travis-ci.org/dhermes/bezier-wheels/settings
[4]: https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml
[5]: https://www.appveyor.com/docs/build-configuration/#secure-variables
[6]: https://ci.appveyor.com/tools/encrypt
[7]: https://cloud.google.com/sdk/install
[8]: https://cloud.google.com/storage/docs/gsutil
[9]: https://pypi.org/project/gsutil/

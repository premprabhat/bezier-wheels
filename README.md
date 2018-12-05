# `bezier-wheels`

[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/dhermes/bezier-wheels?svg=true)](https://ci.appveyor.com/project/dhermes/bezier-wheels)
[![Travis CI Build Status](https://travis-ci.org/dhermes/bezier-wheels.svg)](https://travis-ci.org/dhermes/bezier-wheels)

Wheel Builder for [`bezier`][1]. This uses [`multibuild`][2] to
create wheels for

- `manylinux` (on Travis CI)
- OS X (on Travis CI)
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

[1]: https://github.com/dhermes/bezier
[2]: https://github.com/matthew-brett/multibuild
[3]: https://travis-ci.org/dhermes/bezier-wheels/settings
[4]: https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml
[5]: https://www.appveyor.com/docs/build-configuration/#secure-variables
[6]: https://ci.appveyor.com/tools/encrypt

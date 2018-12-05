# `bezier-wheels`

Wheel Builder for [`bezier`][1]. This uses [`multibuild`][2] to
create wheels for

- `manylinux` (on Travis)
- OS X (on Travis)
- Windows (on AppVeyor)

and uploads the built wheels to a Google Cloud Storage bucket specified
in the Travis and AppVeyor configurations.

[1]: https://github.com/dhermes/bezier
[2]: https://github.com/matthew-brett/multibuild

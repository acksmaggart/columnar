# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
**[1.4.1] 2021-12-27**
- Added
  - A check for an empty input list which will produce a type error.
  - A test file compatible with pytest. (Thanks to @wontonst!)

**[1.4.0] 2021-12-27**
- Added
  - A changelog.
  - A new boolean argument called `preformatted_headers` which, when `no_borders==True` will use the headers as-provided, rather than captializing the headers.

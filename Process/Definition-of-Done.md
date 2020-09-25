A PBI will be considered "Done" when
* any code changes are merged into `master` branch 
* the work has been verified with the Product Owner
* the work has been reviewed by the developer and 2 additional team members (see [Git Flow](/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/-/wikis/Process/Git%20Flow))
* all tests have passed
* the work meets the acceptance criteria
* appropriate tests (at least 1) have been written to test the code changes
* code analyzers and linters ensure the code has not regressed and is within an acceptable range of "cleanness"
    * If `ESLint` is used: no warnings and no errors
    * If `pylint` is used: the score should not be below 8 / 10
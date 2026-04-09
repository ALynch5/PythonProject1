# Toolchain Critique

## Overview

For this project, we used a range of tools including Flask, PostgreSQL, Docker, and GitHub Actions.

Since this was our first time using most of these tools, we focused on getting them working rather than using advanced features.

---

## What worked well

One of the main things that worked well was GitHub.

Using GitHub made it easy for us to:

* manage our code
* work on different parts at the same time
* review each other’s work

Pull requests were especially useful because they helped us to avoid mistakes before merging code.

---

Docker was also useful.

It allowed us to run the project in a consistent way, without worrying about differences between machines.

---

GitHub Actions helped us to automate parts of the project.

Even though our setup was simple, it showed us how CI/CD works and how code can be tested automatically, which we found really useful.

---

## Challenges

Some tools were difficult at the start.

Docker was confusing at first, especially understanding how the containers work.

Setting up CI/CD with GitHub Actions was also challenging because we had to learn the workflow syntax.

Working with environment variables was also new to us, and even though this project was simple, we had to make sure not to expose sensitive information as practice for potentially bigger projects in the future.
During the project, we actually received a warning email from Supabase about a security issue, which helped us to understand how important it is to protect things like database credentials, and we fixed the issue as part of the process.
---

## Limitations

Our use of the tools was quite basic.

For example:

* our CI/CD pipeline is simple
* we don’t have too many automated tests
* logging and monitoring are minimal

This means the project would need improvements before being used in a real production environment.

---

## What we would improve

If we had more time, we would:

* add more automated tests
* improve the CI/CD pipeline
* add better logging and monitoring
* explore more advanced Docker features

---

## Conclusion

Overall, the tools we used were effective for building a simple application.

Even though we only used basic features, this project helped us understand how these tools work together in a real development workflow.

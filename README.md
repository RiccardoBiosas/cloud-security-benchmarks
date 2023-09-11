# Cloud Security Benchmarks

Benchmark DevSecOps tools against vulnerable cloud/IaC target resources.

### Monorepo
- [core](core/README.md) -  collection of packages that is organized by the types of DevSecOps tools they contain (i.e.: IaC scanners, DAST, IAM scanners etc.).

### Targets
- [terragoat](https://github.com/bridgecrewio/terragoat): git submodule pointing to Terragoat - a collection of vulnerable Terraform configurations
- [kubernetes-goat](https://github.com/madhuakula/kubernetes-goat): git submodule pointing to kubernetes-goat - a collection of vulnerable Kubernetes clusters
- []() : - a vulnerable by design Python codebase
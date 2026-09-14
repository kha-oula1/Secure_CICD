<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a Secure CI/CD Pipeline

**Project Link:** [View Project](https://nextwork.ai/projects/fd3f2e33-630f-46a7-9a84-026efcafa493)

**Author:** Khaoula Belhadj  
**Email:** belhadjkhaoula07@gmail.com

---

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/fd3f2e33-630f-46a7-9a84-026efcafa493_elvulgp5)

## Delivering a Traceable Container Artifact

### Documenting the CI/CD workflow

In this step, I'm publishing a public image through GitHub Container Registry before pulling it into WSL.

### Evidence of pipeline security and delivery

it proves the pipeline's structural guarantees (gating, scoping, tagging, isolation) because those are enforceable directly from the YAML, and it proves the build/runtime distinction because we just watched it happen. But the production-safety claims (ECS behavior, "not accessed") are inferences from the absence of deploy steps — solid, but only as strong as the actual ci.yml and ECS config being what the doc says they are.

## Validating a Production-Ready Container Safely

### Isolating runtime configuration and delivery permissions

In this step, Start the SQS consumer only when an upload queue is configured.
Supply disposable runtime configuration to the smoke-test container.
Add a least-privilege publishing job for successful pushes to main.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/fd3f2e33-630f-46a7-9a84-026efcafa493_6vnbxqa8)

## Proving the Repository Builds Cleanly in CI

### Creating the first GitHub Actions validation workflow

In this step, I'm creating a workflow that builds the DentalFlow image and compiles its Python source and push the workflow and inspect its first green validation run.

### Keeping unnecessary and sensitive files out of builds

The .dockerignore file excludes unnecessary and sensitive files from the Docker build context. It keeps out Python cache files (__pycache__/, *.py[cod]), database files (*.db), environment variable files (.env), virtual environments (.venv/), and pytest cache files (.pytest_cache/). This reduces the build context size, speeds up Docker builds, and prevents sensitive or temporary files from being included in the image.

### What a green remote build demonstrates

The green remote build proves that the repository’s CI/CD pipeline runs successfully on the remote server, and that the code can be built and validated automatically without errors in the configured environment.


![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/fd3f2e33-630f-46a7-9a84-026efcafa493_rb9zx18e)

## Turning Startup Failures into Actionable Evidence

### Adding a container health smoke test

In this step, i'm adding a container smoke test to the validation job.
Add an always-running cleanup step for logs.
Push the workflow to diagnose the remote startup result.

### Why a successful build is not runtime proof

The container smoke test proved that the Docker image builds successfully

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/fd3f2e33-630f-46a7-9a84-026efcafa493_zhxtyj5t)

## Establishing a Safe CI Development Environment

### Verifying the branch, repository, and Docker environment

In this step, I'll open the local DentalFlow repository in Visual Studio Code through WSL.
Verify the local development foundation.
Create feature/ci-container-pipeline as the isolated working branch.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/fd3f2e33-630f-46a7-9a84-026efcafa493_g3qp7e9q)

## Enforcing Quality Gates on Main

### Protecting main from unvalidated changes

In this project extension, I enforced changes by pairing CI validation with branch protection so a red pipeline could never reach main unnoticed.

![Image](https://nextwork.ai/courageous_silver_serene_goblin/uploads/fd3f2e33-630f-46a7-9a84-026efcafa493_1h9bxwxc)

## Defining the CI/CD Delivery Goal

### Validating changes without deploying to live infrastructure

I'm building, testing, and publishing a Docker image with GitHub Actions and GHCR.





## Reflecting on CI/CD Skills Gained

### Tools and concepts applied

git
docker
github action 
GHCR

### Project effort and challenge

This project took me approximately 1h30min and the most challenging part was fix runtime isolation

### Next learning goal

I did this project today to learn how to config github action .

---

*Built with [NextWork](https://nextwork.ai) - [View this project](https://nextwork.ai/projects/fd3f2e33-630f-46a7-9a84-026efcafa493)*

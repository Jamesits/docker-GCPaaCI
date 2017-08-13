# docker-GCPaaCI

Push Google Cloud Platform docker build status to GitHub like a CI.

## Usage

Put this in `gcloud.yml`:

```yaml
steps:
# ...after your image build step
- name: 'jamesits/docker-gcpaaci'
  args:
  - 'ci'
  - '--auth=github_username:password'
  - '--repo=github_username/repo'
  - '--commit-hash=$COMMIT_SHA'
  - '--state=success'
  - '--description="build finished"'
```
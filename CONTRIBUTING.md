# Contributing to CIS Team Roadmaps

Thank you for helping learners in the 2026–2027 season.

## Choose your contribution

- Submit a new roadmap or improve an existing one.
- Suggest a resource, correct an error, or report a broken link.
- Propose a new track using the roadmap proposal issue template.

Check existing issues and pull requests to avoid duplicating work. If someone is already working on the topic, coordinate in that issue.

## Submit through the GitHub website

1. Fork this repository into your account.
2. In your fork, create a branch such as `roadmap/frontend-react`.
3. Copy [the template](templates/ROADMAP_TEMPLATE.md).
4. Open the appropriate track folder and choose **Add file → Create new file**. Use a descriptive name, for example `react-roadmap.md`, and paste your completed roadmap.
5. Commit the file to your branch. Add a relative link to it in that track's `README.md`.
6. Open **Contribute → Open pull request**, targeting `CIS-Team/2026-2027-Roadmaps` on `main`.
7. Complete the pull request checklist. Use a draft PR if you are still writing.
8. Respond to review feedback. A maintainer will merge the accepted contribution.

Contributors who already have write access can create a branch in this repository and follow the same pull request process.

## File organization

Keep the existing track names. Use lowercase, hyphen-separated filenames such as `nodejs-roadmap.md`. Put supporting images in an `assets/` subfolder within the track and use relative links. Keep files small and avoid uploading videos, course archives, or generated project dependencies.

A Markdown roadmap should remain readable without opening a PDF or external tool. If supplying a PDF, include a Markdown overview covering prerequisites, outcomes, stages, contributor credits, and a link to the PDF.

## Content checklist

- Explain the intended audience, prerequisites, and measurable outcomes.
- Order topics logically and distinguish required topics from optional ones.
- Give realistic time estimates with weekly effort assumptions; avoid job guarantees.
- Include practical exercises and at least one final project.
- Describe each resource and label its language and whether it is free, paid, or freemium.
- Open and check all links before submission; record the review date.
- Credit original sources and contributors. Do not copy material without permission.
- Remove template instructions and unfilled placeholders.
- Add your roadmap to the track index. Change the root track status to **Available** when the first complete roadmap is ready for merge.

English and Arabic contributions are welcome; state the roadmap language and resource languages clearly.

## Review

Keep each PR focused on one roadmap or one related improvement. Maintainers may request edits before merging. A roadmap being merged means it is available for learners; it does not guarantee that third-party resources will remain current.

Please keep discussion respectful and constructive. Do not include passwords, access tokens, private learner information, or materials you cannot share publicly.

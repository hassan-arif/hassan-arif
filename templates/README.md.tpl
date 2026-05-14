# 👨🏻‍💻 [Hassan Mahmood](https://linkedin.com/in/ihassanmahmood)

[![GitHub followers](https://img.shields.io/github/followers/hassan-arif?label=Follow&style=social)](https://github.com/hassan-arif/?tab=follow)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-%230077B5.svg)](https://www.linkedin.com/in/ihassanmahmood/)
[![Portfolio Badge](https://img.shields.io/badge/Portfolio-%234d8fcc.svg)](https://hassan-arif.github.io/portfolio/)

[![wakatime](https://wakatime.com/badge/user/8c559fa0-fa9f-424b-b7e9-f23470599396.svg)](https://wakatime.com/@8c559fa0-fa9f-424b-b7e9-f23470599396)
[![ProfileViews](https://komarev.com/ghpvc/?username=hassan-arif&color=red&style=flat)](https://komarev.com/ghpvc/?username=hassan-arif)

👋 Hello! I love learning technologies, building softwares, and automating my workflows. From design to development I love the entire process of building software. I focus on maintainability, performance, and security with all of my projects and try to follow a lot of best practices. Following best practices early on is the way to go and I'm a huge supporter of it.

<sub>_open to interesting work_</sub>

{{with recentRepos 10}}
#### 🌱 My latest projects
{{range .}}
- [{{.Name}}]({{.URL}}) - {{.Description}}
{{- end}}
{{end}}

{{with recentContributions 10}}
#### 👷 Check out what I'm currently working on
{{range .}}
- [{{.Repo.Name}}]({{.Repo.URL}}) - {{.Repo.Description}} ({{humanize .OccurredAt}})
{{- end}}
{{end}}

{{with recentPullRequests 5}}
#### 🔨 My recent Pull Requests
{{range .}}
- [{{.Title}}]({{.URL}}) on [{{.Repo.Name}}]({{.Repo.URL}}) ({{humanize .CreatedAt}})
{{- end}}
{{end}}

{{with recentReleases 5}}
#### 🚀 Latest releases I've contributed to
{{range .}}
- [{{.Name}}]({{.URL}}) ([{{.LastRelease.TagName}}]({{.LastRelease.URL}}), {{humanize .LastRelease.PublishedAt}}){{ with .Description }} - {{.}}{{ end }}
{{- end}}
{{end}}

{{with recentStars 5}}
#### ⭐ Recent Stars
{{range .}}
- [{{.Repo.Name}}]({{.Repo.URL}}) - {{.Repo.Description}} ({{humanize .StarredAt}})
{{- end}}
{{end}}

<!-- ![](https://github-readme-stats.vercel.app/api?username=hassan-arif&theme=vision-friendly-dark&hide_border=false&include_all_commits=true&count_private=true) -->

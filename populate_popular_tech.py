import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cheatsheets_project.settings')
django.setup()

from core.models import Technology, CheatSheet, Category

def populate():
    # Clear existing data to avoid duplicates/mess
    print("Cleaning up old data...")
    Category.objects.all().delete()
    Technology.objects.all().delete()

    categories = {
        "Web Frontend": {
            "icon": "fa-solid fa-code",
            "technologies": [
                ("HTML5", "html5", "fa-brands fa-html5", [
                    {"title": "HTML5 Cheat Sheet", "url": "https://htmlhead.dev/"},
                    {"title": "MDN HTML Reference", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"}
                ]),
                ("CSS3", "css3", "fa-brands fa-css3-alt", [
                    {"title": "CSS Grid & Flexbox", "url": "https://adam-marsden.co.uk/css-cheat-sheet"},
                    {"title": "MDN CSS Reference", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS"}
                ]),
                ("JavaScript", "javascript", "fa-brands fa-js", [
                    {"title": "JS Quick Ref", "url": "https://quickref.me/javascript"},
                    {"title": "Modern JS Cheatsheet", "url": "https://mbeaudru.github.io/modern-js-cheatsheet/"}
                ]),
                ("React", "react", "fa-brands fa-react", [
                    {"title": "React Cheatsheet", "url": "https://devhints.io/react"},
                    {"title": "React Official Docs", "url": "https://react.dev/reference/react"}
                ]),
                ("Vue.js", "vuejs", "fa-brands fa-vuejs", [
                    {"title": "Vue 3 Cheatsheet", "url": "https://devhints.io/vue"},
                    {"title": "Vue Guide", "url": "https://vuejs.org/guide/introduction.html"}
                ]),
                ("Angular", "angular", "fa-brands fa-angular", [
                    {"title": "Angular Cheatsheet", "url": "https://angular.io/guide/cheatsheet"}
                ]),
                ("TypeScript", "typescript", "fa-solid fa-code", [
                    {"title": "TypeScript Cheatsheet", "url": "https://devhints.io/typescript"}
                ]),
                ("Bootstrap", "bootstrap", "fa-brands fa-bootstrap", [
                    {"title": "Bootstrap 5 Docs", "url": "https://getbootstrap.com/docs/5.3/getting-started/introduction/"}
                ]),
                ("Tailwind CSS", "tailwindcss", "fa-solid fa-wind", [
                    {"title": "Tailwind Cheat Sheet", "url": "https://nerdcave.com/tailwind-cheat-sheet"}
                ]),
                ("Svelte", "svelte", "fa-solid fa-code", [
                    {"title": "Svelte Cheatsheet", "url": "https://sveltesociety.dev/cheatsheet"}
                ]),
            ]
        },
        "Web Backend": {
            "icon": "fa-solid fa-server",
            "technologies": [
                ("Node.js", "nodejs", "fa-brands fa-node", [
                    {"title": "Node.js Docs", "url": "https://nodejs.org/en/docs/"},
                    {"title": "DevHints Node.js", "url": "https://devhints.io/nodejs"}
                ]),
                ("Express", "express", "fa-brands fa-node-js", [
                    {"title": "Express Docs", "url": "https://expressjs.com/"},
                    {"title": "DevHints Express", "url": "https://devhints.io/express"}
                ]),
                ("Django", "django", "fa-solid fa-code", [
                    {"title": "Django Cheatsheet", "url": "https://django-cheatsheet.jboy.edu.es/"},
                    {"title": "Official Docs", "url": "https://docs.djangoproject.com/en/stable/"}
                ]),
                ("Flask", "flask", "fa-solid fa-flask", [
                    {"title": "Flask Cheatsheet", "url": "https://www.pythoncheatsheet.org/web-development/flask"},
                    {"title": "Official Docs", "url": "https://flask.palletsprojects.com/"}
                ]),
                ("PHP", "php", "fa-brands fa-php", [
                    {"title": "PHP Manual", "url": "https://www.php.net/manual/en/langref.php"},
                    {"title": "PHP Cheatsheet", "url": "https://phpcheatsheets.com/"}
                ]),
                ("Laravel", "laravel", "fa-brands fa-laravel", [
                    {"title": "Laravel Docs", "url": "https://laravel.com/docs/10.x"},
                    {"title": "Laravel Cheatsheet", "url": "https://laravel-cheatsheet.com/"}
                ]),
                ("Ruby", "ruby", "fa-solid fa-gem", [
                    {"title": "Ruby Docs", "url": "https://www.ruby-lang.org/en/documentation/quickstart/"},
                    {"title": "Ruby Cheatsheet", "url": "https://quickref.me/ruby"}
                ]),
                ("Rails", "rails", "fa-solid fa-gem", [
                    {"title": "Rails Guides", "url": "https://guides.rubyonrails.org/"},
                    {"title": "Rails Cheatsheet", "url": "https://devhints.io/rails"}
                ]),
                ("ASP.NET Core", "aspnet-core", "fa-brands fa-microsoft", [
                    {"title": "ASP.NET Core Docs", "url": "https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-7.0"},
                    {"title": "DotNetCore Cheatsheet", "url": "https://cheatography.com/amenon/cheat-sheets/asp-net-core-mvc/"}
                ]),
            ]
        },
        "Programming Languages": {
            "icon": "fa-solid fa-terminal",
            "technologies": [
                ("Python", "python", "fa-brands fa-python", [
                    {"title": "Python Cheatsheet", "url": "https://www.pythoncheatsheet.org/"},
                    {"title": "Official Docs", "url": "https://docs.python.org/3/"}
                ]),
                ("Java", "java", "fa-brands fa-java", [
                    {"title": "Java Cheatsheet", "url": "https://introcs.cs.princeton.edu/java/11cheatsheet/"},
                    {"title": "Oracle Java Docs", "url": "https://docs.oracle.com/en/java/"}
                ]),
                ("C", "c", "fa-solid fa-c", [
                    {"title": "C Cheatsheet", "url": "https://courses.cs.washington.edu/courses/cse351/18wi/materials/cheatsheet-c.pdf"},
                    {"title": "C Reference", "url": "https://en.cppreference.com/w/c"}
                ]),
                ("C++", "cpp", "fa-solid fa-code", [
                    {"title": "C++ Cheatsheet", "url": "https://www.geeksforgeeks.org/c-plus-plus-cheat-sheet/"},
                    {"title": "C++ Reference", "url": "https://en.cppreference.com/w/"}
                ]),
                ("C#", "csharp", "fa-brands fa-microsoft", [
                    {"title": "C# Docs", "url": "https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/"},
                    {"title": "C# Cheatsheet", "url": "https://cheatography.com/laurence/cheat-sheets/c-sharp/"}
                ]),
                ("Go", "go", "fa-brands fa-golang", [
                    {"title": "Go Cheatsheet", "url": "https://devhints.io/go"},
                    {"title": "Go Docs", "url": "https://go.dev/doc/"}
                ]),
                ("Rust", "rust", "fa-brands fa-rust", [
                    {"title": "Rust Cheatsheet", "url": "https://cheats.rs/"},
                    {"title": "Rust Docs", "url": "https://doc.rust-lang.org/book/"}
                ]),
                ("Swift", "swift", "fa-brands fa-swift", [
                    {"title": "Swift Cheatsheet", "url": "https://github.com/raywenderlich/swift-cheat-sheet"},
                    {"title": "Swift Docs", "url": "https://www.swift.org/documentation/"}
                ]),
                ("Kotlin", "kotlin", "fa-brands fa-android", [
                    {"title": "Kotlin Docs", "url": "https://kotlinlang.org/docs/reference/"},
                    {"title": "Kotlin Cheatsheet", "url": "https://developer.android.com/kotlin/cheat-sheet"}
                ]),
                ("Lua", "lua", "fa-solid fa-moon", [
                    {"title": "Lua Cheatsheet", "url": "https://devhints.io/lua"},
                    {"title": "Lua Docs", "url": "https://www.lua.org/manual/5.4/"}
                ]),
                ("R", "r", "fa-solid fa-chart-simple", [
                    {"title": "RStudio Cheatsheets", "url": "https://www.rstudio.com/resources/cheatsheets/"},
                    {"title": "R Docs", "url": "https://www.rdocumentation.org/"}
                ]),
                ("Matlab", "matlab", "fa-solid fa-square-root-variable", [
                    {"title": "Matlab Academy", "url": "https://matlabacademy.mathworks.com/"},
                    {"title": "Matlab Docs", "url": "https://www.mathworks.com/help/matlab/"}
                ]),
                ("Scala", "scala", "fa-solid fa-code", [
                    {"title": "Scala Cheatsheet", "url": "https://docs.scala-lang.org/cheatsheets/"},
                    {"title": "Scala Docs", "url": "https://docs.scala-lang.org/"}
                ]),
                ("Perl", "perl", "fa-solid fa-code", [
                    {"title": "Perl Docs", "url": "https://learn.perl.org/docs/"},
                    {"title": "Perl Cheatsheet", "url": "https://devhints.io/perl"}
                ]),
                ("Haskell", "haskell", "fa-solid fa-code", [
                    {"title": "Haskell Cheatsheet", "url": "https://cheatsheet.codeslower.com/"},
                    {"title": "Haskell Docs", "url": "https://www.haskell.org/documentation/"}
                ]),
                ("Elixir", "elixir", "fa-solid fa-fire", [
                    {"title": "Elixir Cheatsheet", "url": "https://devhints.io/elixir"},
                    {"title": "Elixir Docs", "url": "https://elixir-lang.org/docs.html"}
                ]),
            ]
        },
        "Databases": {
            "icon": "fa-solid fa-database",
            "technologies": [
                ("MySQL", "mysql", "fa-solid fa-database", [
                    {"title": "MySQL Cheatsheet", "url": "https://devhints.io/mysql"},
                    {"title": "MySQL Documentation", "url": "https://dev.mysql.com/doc/"}
                ]),
                ("PostgreSQL", "postgresql", "fa-solid fa-database", [
                    {"title": "Postgres Cheatsheet", "url": "https://postgrescheatsheet.com/"},
                    {"title": "PostgreSQL Docs", "url": "https://www.postgresql.org/docs/"}
                ]),
                ("MongoDB", "mongodb", "fa-solid fa-leaf", [
                    {"title": "MongoDB Cheatsheet", "url": "https://www.mongodb.com/developer/products/mongodb/cheat-sheet/"},
                    {"title": "MongoDB Manual", "url": "https://www.mongodb.com/docs/manual/"}
                ]),
                ("Redis", "redis", "fa-solid fa-database", [
                    {"title": "Redis Cheatsheet", "url": "https://lzone.de/cheat-sheet/Redis"},
                    {"title": "Redis Docs", "url": "https://redis.io/docs/"}
                ]),
                ("SQLite", "sqlite", "fa-solid fa-database", [
                    {"title": "SQLite Tutorial", "url": "https://www.sqlitetutorial.net/sqlite-cheat-sheet/"},
                    {"title": "SQLite Docs", "url": "https://www.sqlite.org/docs.html"}
                ]),
                ("SQL", "sql", "fa-solid fa-database", [
                    {"title": "SQL Cheatsheet", "url": "https://www.sqltutorial.org/sql-cheat-sheet/"},
                    {"title": "W3Schools SQL", "url": "https://www.w3schools.com/sql/"}
                ]),
            ]
        },
        "DevOps & Tools": {
            "icon": "fa-solid fa-gears",
            "technologies": [
                ("Git", "git", "fa-brands fa-git-alt", [
                    {"title": "Git Cheatsheet", "url": "https://education.github.com/git-cheat-sheet-education.pdf"},
                    {"title": "Git Docs", "url": "https://git-scm.com/doc"}
                ]),
                ("Docker", "docker", "fa-brands fa-docker", [
                    {"title": "Docker Cheatsheet", "url": "https://docs.docker.com/get-started/docker_cheatsheet.pdf"},
                    {"title": "Docker Docs", "url": "https://docs.docker.com/"}
                ]),
                ("Kubernetes", "kubernetes", "fa-solid fa-dharmachakra", [
                    {"title": "Kubectl Cheatsheet", "url": "https://kubernetes.io/docs/reference/kubectl/cheatsheet/"},
                    {"title": "Kubernetes Docs", "url": "https://kubernetes.io/docs/home/"}
                ]),
                ("Linux", "linux", "fa-brands fa-linux", [
                    {"title": "Linux Cheatsheet", "url": "https://devhints.io/linux"},
                    {"title": "Linux Kernel Docs", "url": "https://www.kernel.org/doc/html/latest/"}
                ]),
                ("Bash", "bash", "fa-solid fa-terminal", [
                    {"title": "Bash Cheatsheet", "url": "https://devhints.io/bash"},
                    {"title": "GNU Bash Manual", "url": "https://www.gnu.org/software/bash/manual/"}
                ]),
                ("PowerShell", "powershell", "fa-solid fa-terminal", [
                    {"title": "PowerShell Cheatsheet", "url": "https://devhints.io/powershell"},
                    {"title": "PowerShell Docs", "url": "https://learn.microsoft.com/en-us/powershell/"}
                ]),
                ("Vim", "vim", "fa-solid fa-terminal", [
                    {"title": "Vim Shortcut", "url": "https://vim.rtorr.com/"},
                    {"title": "Vim Docs", "url": "https://www.vim.org/docs.php"}
                ]),
                ("Regex", "regex", "fa-solid fa-code", [
                    {"title": "Regex Cheatsheet", "url": "https://cheatography.com/davechild/cheat-sheets/regular-expressions/"},
                    {"title": "RegexOne", "url": "https://regexone.com/"}
                ]),
                ("Markdown", "markdown", "fa-brands fa-markdown", [
                    {"title": "Markdown Guide", "url": "https://www.markdownguide.org/cheat-sheet/"},
                    {"title": "CommonMark Spec", "url": "https://spec.commonmark.org/"}
                ]),
                ("AWS", "aws", "fa-brands fa-aws", [
                    {"title": "AWS Cheatsheet", "url": "https://digitalcloud.training/aws-cheat-sheets/"},
                    {"title": "AWS Documentation", "url": "https://docs.aws.amazon.com/"}
                ]),
                ("Azure", "azure", "fa-brands fa-microsoft", [
                    {"title": "Azure Products", "url": "https://learn.microsoft.com/en-us/azure/?product=popular"},
                    {"title": "Azure Docs", "url": "https://learn.microsoft.com/en-us/azure/"}
                ]),
            ]
        },
        "Data Science & AI": {
            "icon": "fa-solid fa-brain",
            "technologies": [
                ("NumPy", "numpy", "fa-solid fa-cube", [
                    {"title": "NumPy PDF", "url": "https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf"},
                    {"title": "NumPy Docs", "url": "https://numpy.org/doc/"}
                ]),
                ("Pandas", "pandas", "fa-solid fa-table", [
                    {"title": "Pandas PDF", "url": "https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf"},
                    {"title": "Pandas Docs", "url": "https://pandas.pydata.org/docs/"}
                ]),
                ("Matplotlib", "matplotlib", "fa-solid fa-chart-line", [
                    {"title": "Matplotlib Cheatsheets", "url": "https://matplotlib.org/cheatsheets/"},
                    {"title": "Matplotlib Docs", "url": "https://matplotlib.org/stable/contents.html"}
                ]),
                ("Scikit-learn", "scikit-learn", "fa-solid fa-brain", [
                    {"title": "Scikit-Learn PDF", "url": "https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Scikit_Learn_Cheat_Sheet_Python.pdf"},
                    {"title": "Scikit-Learn Docs", "url": "https://scikit-learn.org/stable/"}
                ]),
                ("TensorFlow", "tensorflow", "fa-brands fa-google", [
                    {"title": "TensorFlow Guide", "url": "https://www.tensorflow.org/extras/tensorflow_2.0_getting_started_guide"},
                    {"title": "TensorFlow Docs", "url": "https://www.tensorflow.org/api_docs"}
                ]),
                ("PyTorch", "pytorch", "fa-solid fa-fire", [
                    {"title": "PyTorch Cheatsheet", "url": "https://pytorch.org/tutorials/beginner/ptcheat.html"},
                    {"title": "PyTorch Docs", "url": "https://pytorch.org/docs/stable/index.html"}
                ]),
            ]
        }
    }

    print(f"Creating categories and technologies...")

    for cat_name, cat_data in categories.items():
        category = Category.objects.create(
            name=cat_name,
            icon=cat_data["icon"]
        )
        print(f"Created Category: {cat_name}")

        for name, slug, icon, resources in cat_data["technologies"]:
            try:
                tech = Technology.objects.create(
                    name=name,
                    slug=slug,
                    category=category,
                    icon=icon,
                    description=f"Cheat sheets and resources for {name}."
                )

                for resource in resources:
                   CheatSheet.objects.create(
                        title=resource["title"],
                        technology=tech,
                        slug=f"{slug}-{django.utils.text.slugify(resource['title'])}",
                        file_type='link',
                        url=resource["url"]
                    )
                
                print(f"Created {name} with {len(resources)} resources")
            except Exception as e:
                print(f"FAILED to create {name}: {e}")

        
    print("Database populated successfully!")

if __name__ == '__main__':
    populate()


# DS105L - Week 09 live experiments

This repository is part of LSE [DS105L 2022/23](https://lse-dsi.github.io/DS105/2023/), for a lecture entitled "🔀 **Merge operations** & 📦 **practical tips for code organisation**". 

The major focus will be on how to work effectively as a group using GitHub, based on the feedback I received from [Shuyu](https://lse-dsi.github.io/DS105/2023/courserep.html) and general interactions with students over Slack/Office Hours.

I could have taken a passive approach and just demonstrate things to you, but I would rather transform this into a workshop where you can learn while practicing.

Here is how it's going to work:

<details><summary><strong>Part ONE</strong></summary>
  
# Part ONE

<details><summary><strong>⚙️ Setup</strong></summary>
  
<p></p>
  
1. I will create a repository from the [jonjoncardoso/data-science-workflow](https://github.com/jonjoncardoso/data-science-workflow) template and I will edit the README.md to remove the template-related text.

2. I will add a Jupyter Notebook with some web scraping code that is not greatly optimised to use pandas as we have been learning in this course...
    
</details>

<details><summary><strong>📋 Create an issue</strong></summary>
<p></p>

3. I will create a [GitHub Issue](https://docs.github.com/en/issues) with a **feature request** to optimise the code.
4. Anyone in the audience will be welcome to **comment** on this GitHub issue with suggestions for code optimisation. 
5. Once we found a solution that we're happy about, we will be ready to close the issue. But I won't close it straightaway!

</details>
  
<details><summary><strong>🌴 Branching</strong></summary>
<p></p>

Instead of modifying it directly in my notebook, I will demonstrate how **groups can work in parallel** on GitHub. 

6. I will open a separate branch, dedicated to that issue, and then I will make my changes there and `git push`
7. Then, I will open a [Pull Request](https://docs.github.com/en/pull-requests) and ask some of you to validate my changes.
8. Once we got approval from you, I will `git merge` changes to `main`
9. We will look at the `git` tree
10. I will tell you about a common practice of using a `develop` vs a `main` branch.

</details>
  
This whole process is a more professional set of practices for using Git and it is commonly known as the [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow.

</details>

<details><summary><strong>Part TWO</strong></summary>
  
# Part TWO

Now I will move my relevant code to a python script and I will invoke it _from_ the Jupyter notebook. **I will explain why and when it is good to do so.** Then, I will open a new issue with an exercise on data pre-processing. Everyone will now try to work out a solution for the exercise using Gitflow!

1. Branch from `develop` and give it a meaningful name.
2. Push your branch to GitHub.
3. Now work on your changes, commit and push them as you like.
4. Once ready, open a pull request from your branch to `develop` and tag me (@jonjoncardoso) as a reviewer.
5. I will review a few and add feedback notes on the spot.
6. Hopefully, some of the solutions will be merged!

</details>

<details><summary><strong>Part THREE</strong> (time allowing)</summary>
  
# Part THREE


- I will demonstrate the use of [GitHub projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- I will show you how I use [GitHub milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones) and how I set deadlines in there.
- I will show you how to [create your own Python package](https://www.pythoncentral.io/how-to-create-a-python-package/) and install it with `pip`.

</details>

<details><summary>🧰 Dev Setup</summary>

## 🧰 Dev Setup

1. Install [Python 3.8](python.org) or higher on your computer.
2. Install [anaconda](https://www.anaconda.com/products/individual) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) (lighter) on your computer.
3. Create a new conda environment:

    ```bash
    conda create -y -n=venv-ds105 python=3.10.8
    ```
4. Activate the environment and make sure you have `pip` installed inside that environment:

  ```console
  # the exact `activate` command will vary depending on your OS
  conda activate venv-ds105
  ```

💡 Remember to activate this particular `conda` environment whenever you reopen VSCode/the terminal.

10. Install required libraries

  ```console
  pip install -r requirements.txt
  ```

Now, whenever you open a Jupyter Notebook, you should see the `venv-ds105` kernel available. 

</details>
  
# 👥 **Contributors**

- [Dr. Jon Cardoso-Silva](http://github.com/jonjoncardoso) is DS105L's course convenour and creator of this exercise!

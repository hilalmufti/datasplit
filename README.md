# datasplit

datasplit is a simple program to split your data into train and test sets.

```
 ____   __  ____  __   ____  ____  __    __  ____ 
(    \ / _\(_  _)/ _\ / ___)(  _ \(  )  (  )(_  _)
 ) D (/    \ )( /    \\___ \ ) __// (_/\ )(   )( 
(____/\_/\_/(__)\_/\_/(____/(__)  \____/(__) (__) 
```

## Usage
Using `datasplit` is really easy. Given a file `data.txt` of the following form:

```
1.1679970026016235 -0.46742919087409973 -0.0226800125092268 0.7523175477981567
-1.2098073959350586 -1.0336159467697144 -0.34529608488082886 -1.5125139951705933
1.2003061771392822 0.04162155091762543 1.4253662824630737 1.8014559745788574
0.8571088910102844 0.8716108798980713 -0.03691474720835686 0.9531587362289429
-1.3668804168701172 -2.220398187637329 -0.35027629137039185 -2.047640323638916
0.5593929886817932 0.5366738438606262 0.04586906358599663 0.6690701842308044
1.6639169454574585 0.5367552638053894 -0.9199331998825073 0.9752432107925415
-1.187464714050293 0.10352841764688492 2.653109312057495 0.6562629342079163
0.33855199813842773 -1.531991720199585 -0.5880853533744812 -0.6132023334503174
0.422885000705719 -0.019597359001636505 0.09082000702619553 0.3783670663833618
```

You can apply `datasplit` to the dataset in `data.txt` with simple Unix pipelines.
That is, one can simply run:

```
cat data.txt | datasplit
```
which will yield the output

```
train 1.1679970026016235 -0.46742919087409973 -0.0226800125092268 0.7523175477981567
train -1.2098073959350586 -1.0336159467697144 -0.34529608488082886 -1.5125139951705933
train 1.2003061771392822 0.04162155091762543 1.4253662824630737 1.8014559745788574
train 0.8571088910102844 0.8716108798980713 -0.03691474720835686 0.9531587362289429
train -1.3668804168701172 -2.220398187637329 -0.35027629137039185 -2.047640323638916
train 0.5593929886817932 0.5366738438606262 0.04586906358599663 0.6690701842308044
train 1.6639169454574585 0.5367552638053894 -0.9199331998825073 0.9752432107925415
train -1.187464714050293 0.10352841764688492 2.653109312057495 0.6562629342079163
train 0.33855199813842773 -1.531991720199585 -0.5880853533744812 -0.6132023334503174
test 0.422885000705719 -0.019597359001636505 0.09082000702619553 0.3783670663833618
```
Notice a few things. First, each line of the input data stream is interpreted as
a separate sample by `datasplit`. Second, by default, `datasplit` splits into a
90% training set, and 10% test set. You can customize this with `datasplit -p`.
Check out other ways you can use `datasplit` via `datasplit -h`.

Finally, you may find it useful to use `datasplit` with the [`xyn`](https://github.com/hilalmufti/xyn)
program.

## Install
Installation requires the Python programming language as well as the PyPI (`pip`) package manager.

### Step 1: Install Python and PyPI (skip this if it's already installed)
Python and PyPI are most likely already installed on your computer. Try executing:
```
python --version
pip --version
```
in your terminal to check if this is the case. 
If they're not installed (that is, one of the above commands yields an error), 
then I highly recommend you install them via `uv`. Run one of the following 
commands in the terminal to install `uv` on your computer:
```
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
More detailed instructions on installing `uv` can be found at `uv`'s [official
documentation](https://docs.astral.sh/uv/getting-started/installation/)

### Step 2: Install `datasplit`
Now that `pip` is installed, we simply run one of the following in the terminal
to install `datasplit`:
```
# using uv
uv pip install https://github.com/hilalmufti/datasplit.git

# using PyPI
pip install https://github.com/hilalmufti/datasplit.git
```

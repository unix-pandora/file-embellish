<hr>

### 将返回 1 个包含 site-packages 目录路径的列表

```
y=$(python -c "import site; sitelist=site.getsitepackages(); print(sitelist[0])");
echo $y;
mv *.pth $y;
```

<hr>

### verified

```
python -c "import sys; print(sys.path)"
```

<hr>

# %%

print(f"If I am inside tools.py, and my __name__ is: {__name__}")

def fast_math(x):
    return x * x

if __name__ == "__main__":
    print("Running a secret test that only happens in tools.py")


# %%

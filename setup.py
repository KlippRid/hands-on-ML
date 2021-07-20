import setuptools

setuptools.setup(
    name="mltools",
    version="0.1.0",
    packages=setuptools.find_packages(),
    install_requires=[
        "jupyter",
        "matplotlib",
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn"
    ],
    setup_requires=['flake8']
    #entry_points={"console_scripts": ["run-ble-server = bleserver.ble_server:main"]},
)
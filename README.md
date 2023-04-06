---

# :boom: PwngoDB - Mongodb Checker

<img src='DNMYTZKPQFPMZSGZM.png'>

> PwngoDB is a simple Python script that checks whether a list of MongoDB URLs are accessible or not. It does this by attempting to connect to each URL using the PyMongo driver, and logging the results to separate files depending on whether the connection was successful or not.

---

## :scroll: Requirements

- Python 3.x
- PyMongo 3.x

> You can install PyMongo by running the following command:

```bash
pip install pymongo
```

## :scroll: Installation

```bash
git clone https://github.com/0x1717/PwngoDB.git && cd PwngoDB/ && chmod +x PwngoDB.py
```

## :pill: Usage

> To use the script, you'll need to create a text file containing a list of MongoDB URLs, one per line. For example:

```bash
mongodb://localhost:27017
mongodb+srv://username:password@localhost
```

> Then, you can run the script from the command line with the following arguments:

```bash
python3 PwngoDB.py -l filename.txt
```

---

## :notebook_with_decorative_cover: Disclaimer

> This script is provided as-is and is not guaranteed to work in all situations. Use at your own risk.

## :page_facing_up: License

> This script is released under the MIT License.

---

> #### Created by 0x1717 aka GYG3S

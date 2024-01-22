# eso_names: Elder Scrolls Universe Names Generator and recommendor

**Introduction:**

The `eso_names` Python package provides two distinct functions, `names_generator` and `names_recommendor`, designed to assist players and modders of Elder Scrolls universe games in generating character names that are lore-friendly and well-suited for the game's universe.

**Features:**

1. **Character Name Generation:**
   - The `names_generator` function allows users to generate character names based on specified parameters such as gender, category (race), starting letter, and quantity.
   - Example Usage:
     ```python
     from eso_names.main import names_generator

     generated_names = names_generator(gender='male', category='Argonian', start_letter='A', quantity=5)
     ```
   - Output:
     ```
     ['Am-Sora', 'AxKela', 'Ashir-Me', 'Asabilhvoy', 'Az-Katus']
     ```

2. **Character Name Recommendation:**
   - The `names_recommendor` function recommends character names by leveraging a database containing 22,000 names from all Elder Scrolls games.
   - Users can specify parameters such as gender, category (race), starting letter, quantity, and similarity thresholds to tailor recommendations.
   - Example Usage:
     ```python
     from eso_names.main import names_recommendor

     recommended_names = names_recommendor(gender='male', category='Nord', start_letter='S', quantity=5, similarity_threshold=5, similar_to='Ragnar')
     ```
   - Output:
     ```
     ['Skeggr', 'Safrid', 'Saergar', 'Svenvar', 'Sigaar']
     ```

**Dependencies:**

- The `names_generator` function requires the loading of the RNN class from the `eso_names.raw_model` module. Ensure that the RNN class is properly imported before using the generator.

   ```python
   from eso_names.raw_model import RNN
   ```

**Important Notes:**

- The character name generator utilizes a character-level Recurrent Neural Network (RNN) trained on a dataset containing names from all Elder Scrolls games. While it serves as a valuable tool for inspiration, generated names may not always be optimal.

**Project Goals:**

The primary goal of this project is to facilitate Elder Scroll games players in creating lore-friendly character names. Additionally, it aims to provide modders with a tool to generate fitting names for their in-game creations.

**Getting Started:**

1. Install the `eso_names` package using the following command:
   ```
   pip install eso_names
   ```

2. Import the required functions in your Python script or Jupyter notebook:

   ```python
   from eso_names.main import names_generator, names_recommendor
   ```

3. Utilize the functions as demonstrated in the examples above to generate or recommend character names.

**Contributing:**

Contributions to the project are welcome! If you encounter issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/ShubhamBhut/ElderScrolls-Universe_name_generator).

Also feel free to check [TODO.md](https://github.com/ShubhamBhut/ElderScrolls-Universe_name_generator/blob/master/TODO.md) to add some ideas or get some ideas to work upon.

### File tree of `eso_names` the pip package:

```
eso_names_package/
│   MANIFEST.in
│   requirements.txt
│   setup.py
│
└───eso_names/
    │   main.py
    │   name_generator_v2.py
    │   name_recommender.py
    │   raw_model.py
    │   __init__.py
    │
    ├───db/
    │       names.csv
    │
    └───model/
            model_2.pth
```

**Disclaimer:**

This project is not affiliated with Bethesda Softworks or any of the Elder Scrolls game. It is an independent tool created by [Shubham Patel](https://github.com/ShubhamBhut).

**License:**

This project is licensed under the [MIT License](LICENSE).

Enjoy generating lore-friendly names for your Elder Scrolls characters and creations!
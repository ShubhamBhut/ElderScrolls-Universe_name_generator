- [ ] Since the loss is not dropping after 2.2, need more in depth data processing. May have to remove some outliner names but it feels a lot of work for little improvement. So it shall be done after version 2.0

- [ ] It would be awesome if the generated names can be filtered out by comparing them with lore names before sending them to user. However, this seems little slow but also seems pretty good idea to avoid non-sensical names.

- [ ] Learning rate of 0.01 doesn't seem harmful but rather helpful with combination of clipping with max_Norm 5. Need to explore more here if it can help improving the model.

- [ ] a realease as pip package

- [ ] a web frontend

- [ ] a main function integrating both recommender and generator to return the required names

- [ ] also need to try out temperature less than 1 for lower loss; though it didn't work previously but need proper confirmed checking

### So far the best working setup has been lr of 0.01 with max_norm=5 and no set temperature value (default=1).
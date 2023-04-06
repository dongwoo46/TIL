CREATE TABLE zoo(
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height ,
  age
);

INSERT INTO zoo
VALUES
  ('gorilla','omnivore',215, 180, 5),
  ('rabbit', 'herbivore', 3, 150,''),
  ('tiger', 'carnivore', 220,115,3),
  ('elephant', 'herbivore', 3800, 280, 10),
  ('dog', 'omnivore', 8, 20, 1),
  ('eagle','carnivore',8, 75,''),
  ('dolphin', 'carnivore', 210, '',3),
  ('alligaotr', 'carnivore', 250, 50,''),
  ('panda', 'herbivore', 80, 90, 2),
  ('pig', 'omnivore',70,45,5);


SELECT name,height FROM zoo;

UPDATE zoo SET height=15 WHERE name='rabbit';

DELETE FROM zoo WHERE eat = 'omnivore';

SELECT * FROM zoo;

DROP TABLE zoo
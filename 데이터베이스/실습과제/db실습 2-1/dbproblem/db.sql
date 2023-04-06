CREATE TABLE animals (
  animal_name TEXT NOT NULL,
  height INT NOT NULL,
  weight INT NOT NULL,
  age INT
);

ALTER TABLE animals ADD COLUMN meal TEXT;

ALTER TABLE animals RENAME TO zoo

DROP TABLE zoo
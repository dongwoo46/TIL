CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 원인은 각 VALUES에 맞는 값이 들어가 있지 않았음 name,eat에는 text가
-- weight,height, age에는 int값을 넣어주면된다.
INSERT INTO zoo (age, height, weight, name, eat) VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2) rowid가 중복되어있음 rowid삭제해줌
INSERT INTO zoo (name, eat, weight, age) VALUES
('dolphin', 'carnivore', 210, 3),
('alligator', 'carnivore', 250, 50);

-- 3) weight라는 not null인 값이 포함되지 않았음 포함시켜줌
INSERT INTO zoo (name, eat, age, weight) VALUES
('dolphin', 'carnivore', 3, 200);
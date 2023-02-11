create table t_test (
    id int,
    val1 varchar,
    val2 varchar
);

insert into t_test values
(1, 'test1', 'asdf'),
(2, 'test2', 'qwer'),
(3, 'test3', 'dfgh'),
(4, 'test4', 'xcvb'),
(5, 'test5', 'zxcv'),
(6, 'test6', 'tyui');

-- read data from csv
CREATE TABLE article AS SELECT * FROM read_csv_auto('data/article.csv');

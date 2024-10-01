create table IF NOT EXISTS entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);
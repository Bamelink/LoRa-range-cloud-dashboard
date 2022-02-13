/***CREATING ALL TABLES*/
CREATE TABLE test_gps_data (
  id          INT          AUTO_INCREMENT             PRIMARY KEY,
  time_stamp  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP  NOT NULL,
  latitude    VARCHAR(255)                            NOT NULL,
  longitude   VARCHAR(255)                            NOT NULL,
  rssi        INT(7)                                  NOT NULL
);

/* Create seperate tables with the same structure */
/* CREATE TABLE new_table LIKE test_gps_data; */

/* Fill test_gps_data with test coordinates */
INSERT INTO test_gps_data (latitude, longitude, rssi)
VALUES ('52.150013', '9.953353', -100),
       ('52.150908', '9.951218', -105),
       ('52.150534', '9.948007', -110),
       ('52.149143', '9.938127', -120),
       ('52.145463', '9.939377', -125),
       ('52.142834', '9.933450', -130),
       ('52.117193', '9.899247', -150);
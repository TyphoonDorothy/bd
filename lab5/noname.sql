USE lab4;

DROP PROCEDURE IF EXISTS insert_genres;

DELIMITER //
CREATE PROCEDURE insert_genres()
BEGIN
	DECLARE num INT DEFAULT 1;
    WHILE num <= 10 DO
		INSERT INTO genre(name) VALUE (CONCAT('NONAME', num));
        SET num = num + 1;
	END WHILE;
END //;
DELIMITER ;

CALL insert_genres()
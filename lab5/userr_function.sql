USE lab4;

DROP FUNCTION IF EXISTS calc_score;

SELECT * FROM review;

DELIMITER //
CREATE FUNCTION calc_score(TYPE VARCHAR(3)) RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
    
    IF TYPE = 'max' THEN
		SELECT MAX(score) INTO result FROM review;
	ELSEIF TYPE = 'min' THEN
		SELECT MIN(score) INTO result FROM review;
	ELSEIF TYPE = 'avg' THEN
		SELECT AVG(score) INTO result FROM review;
	ELSEIF TYPE = 'sum' THEN
		SELECT SUM(score) INTO result FROM review;
	ELSE 
		SIGNAL SQLSTATE '45000'
        SET message_text = 'Invalid command';
	END IF;
    
    RETURN result;
END //
DELIMITER ;

SELECT calc_score('avg')

USE lab4;

DROP TRIGGER IF EXISTS insert_len;
DROP TRIGGER IF EXISTS delete_len;

DELIMITER //
CREATE TRIGGER insert_len
AFTER INSERT ON review
FOR EACH ROW
BEGIN
	DECLARE rows_count INT DEFAULT 0;
    SELECT COUNT(*) INTO rows_count FROM review;
    
    IF rows_count < 6 THEN
		SIGNAL SQLSTATE '45000' 
		SET MESSAGE_TEXT = 'Cannot have fewer then 6 rows';
	END IF;
END //

CREATE TRIGGER delete_len
BEFORE DELETE ON review FOR EACH ROW
BEGIN
	DECLARE rows_count INT DEFAULT 0;
    SELECT COUNT(*) INTO rows_count FROM review;
    
    IF rows_count <= 6 THEN
        SIGNAL SQLSTATE '45000' 
		SET MESSAGE_TEXT = 'Cannot have fewer then 6 rows';
	END IF;
END //
DELIMITER ;
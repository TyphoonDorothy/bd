USE lab4;

DROP TRIGGER IF EXISTS insert_fk;
DROP TRIGGER IF EXISTS update_fk;
DROP TRIGGER IF EXISTS delete_fk;

DELIMITER //
CREATE TRIGGER insert_fk
BEFORE INSERT ON nomination
FOR EACH ROW
BEGIN 
	DECLARE award_exists INT;
    SELECT COUNT(*) INTO award_exists FROM award 
    WHERE award.id = NEW.award_id;
    IF award_exists = 0 THEN
		SIGNAL SQLSTATE '45000' 
		SET MESSAGE_TEXT = 'Award does not exist';
    END IF;
END //

CREATE TRIGGER update_fk
BEFORE UPDATE ON nomination
FOR EACH ROW
BEGIN 
	DECLARE award_exists INT;
    SELECT COUNT(*) INTO award_exists FROM award 
    WHERE award.id = new.award_id;
    IF award_exists = 0 THEN
		SIGNAL SQLSTATE '45000' 
		SET MESSAGE_TEXT = 'Award does not exist';
    END IF;
END //

CREATE TRIGGER delete_fk
BEFORE DELETE ON award
FOR EACH ROW
BEGIN
    DECLARE nomination_exists INT;
    SELECT COUNT(*) INTO nomination_exists
    FROM nomination
    WHERE nomination.award_id = OLD.id;

    IF nomination_exists > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete award because it is referenced in nominations';
    END IF;
END //
DELIMITER ;
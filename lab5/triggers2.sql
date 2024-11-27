USE lab4;

DROP TRIGGER IF EXISTS insert_name;
DROP TRIGGER IF EXISTS update_name;

DELIMITER //
CREATE TRIGGER insert_name
BEFORE INSERT ON director
FOR EACH ROW
BEGIN
    IF NOT (NEW.name IN ('Oksana', 'Olha', 'Petro', 'Taras')) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid name';
    END IF;
END //

CREATE TRIGGER update_name
BEFORE UPDATE ON director
FOR EACH ROW
BEGIN
    IF NOT (NEW.name IN ('Oksana', 'Olha', 'Petro', 'Taras')) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid name';
    END IF;
END //
DELIMITER ;

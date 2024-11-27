USE lab4;

DROP TRIGGER IF EXISTS forbid_insert;
DROP TRIGGER IF EXISTS forbid_update;
DROP TRIGGER IF EXISTS forbid_delete;

DELIMITER //

CREATE TRIGGER forbid_insert
BEFORE INSERT ON festival
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification of data is not allowed in this table';
END //

CREATE TRIGGER forbid_update
BEFORE UPDATE ON festival
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification of data is not allowed in this table';
END //

CREATE TRIGGER forbid_delete
BEFORE DELETE ON festival
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification of data is not allowed in this table';
END //

DELIMITER ;

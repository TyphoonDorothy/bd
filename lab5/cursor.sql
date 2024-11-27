DROP DATABASE IF EXISTS cursor_db;

CREATE DATABASE cursor_db;
USE cursor_db;

DELIMITER //
CREATE PROCEDURE create_dynamic_tables()
BEGIN
	DECLARE done INT DEFAULT 0;
    DECLARE movie_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM lab4.movie;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    OPEN cur;
    
    read_loop: LOOP
		FETCH cur INTO movie_id;
        IF done THEN
			LEAVE read_loop;
		END IF;
        
        SET @current_timestamp = DATE_FORMAT(NOW(), '%Y%m%d%H%i%s');
        SET @table_name = CONCAT('Movie', movie_id, '_', @current_timestamp);
        SET @num_columns = FLOOR(1 + RAND() * 9);
        SET @columns = '';
        
        SET @i = 1;
        WHILE @i <= @num_columns DO
            SET @column_name = concat('col', @i);
            SET @column_type = 'int';
            SET @columns = concat(@columns, @column_name, ' ', @column_type, if(@i < @num_columns, ', ', ''));
            SET @i = @i + 1;
        END WHILE;
        
        SET @create_table_sql = CONCAT('create table ', @table_name, ' (id int auto_increment primary key, ', @columns, ')');
        PREPARE stmt FROM @create_table_sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

    END LOOP;

    CLOSE cur;
END //

DELIMITER ;

CALL create_dynamic_tables();
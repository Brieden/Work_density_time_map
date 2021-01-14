-- SPATIAL QUERY FOR THE Work Diversity Map
SELECT load_extension('mod_spatialite');
.header on
.mode csv
.once result.csv
SELECT A.yr, AsText(ST_Transform(A.geometryLV95, 4326)) AS wkt, 
A.B08VZAT from gstatent as A 
WHERE (A.yr=='2015' AND Within(A.geometryLV95,Buffer(GeomFromText('Point(2683268 1248001)'), 5000)));
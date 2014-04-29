id
name
desc       => description, desc is an alias
url
thumbnail  => Paperclip has_attached :thumbnail with image processing
collab_ext => external_collaborator, collab_ext is an alias
client     => should it be a model/table?
funding_id => belongs_to :funding
timing     => seems to be a confused / useless field
status     => should be calculated from start/end dates
municipalities_type => handling with better relationships
equity         => What question does this answer?
equity_comment => What question does this answer?
active         => should be calculated from start/end dates
last_modified  => updated_at
created        => created_at
start_date
end_date






title:string
description:text
url:string
thumbnail:attachment
external_collaborator:string
client:string
funding_id:integer
status:string
equity_focus:boolean
equity_comment:text
start_date:datetime
end_date:datetime


name AS title, desc AS description, url, thumbnail AS thumbnail_file_name, collab_ext AS external_collaborator, client, funding_id, status, equity AS equity_focus, equity_comment, active, last_modified AS updated_at, created AS created_at, start_date, end_date


desc AS description,

COPY (SELECT id, name AS title, url, thumbnail AS thumbnail_file_name, collab_ext AS external_collaborator, client, funding_id, status, equity AS equity_focus, equity_comment, active, last_modified AS updated_at, created AS created_at, start_date, end_date FROM projects_project ORDER BY id ASC) TO '/tmp/mf_sample_projects.csv' DELIMITER ',' CSV HEADER;

COPY (SELECT * FROM projects_project ORDER BY id ASC) TO '/tmp/mf_all_desc.csv' DELIMITER ',' CSV HEADER;




shp2pgsql -c -g geom -s 4326 -I mapc_subregions_simpl.shp gisdata.subregions_simple > subregions_simple.sql



COPY (SELECT gid AS id, muni_id, municipal AS name, ST_AsText(geom) AS geom FROM gisdata.subregions_simple) TO '/Users/mapcuser/Projects/MetroFuture In Action/in-action/db/fixtures/geometries/subregions/sr.csv' DELIMITER ',' CSV HEADER;


Projects joined to Municipality information

SELECT
  projects_municipality.muni_id AS municipality_id,
  projects_project_municipalities.project_id AS project_id
FROM
  projects_municipality
INNER JOIN
  projects_project_municipalities ON projects_municipality.muni_id = projects_project_municipalities.municipality_id
ORDER BY
  projects_project_municipalities.project_id ASC


Projects joined to Subregion information

SELECT
  projects_subregion.id AS subregion_id,
  projects_project_subregions.project_id AS project_id
FROM
  projects_subregion
INNER JOIN
  projects_project_subregions ON projects_subregion.id = projects_project_subregions.subregion_id
ORDER BY
  projects_project_subregions.project_id ASC


SELECT
  projects_municipality.muni_id,
  projects_municipality_subregion.municipality_id,
  projects_municipality_subregion.subregion_id
FROM
  projects_municipality
INNER JOIN
  projects_municipality_subregion ON projects_municipality.muni_id = projects_municipality_subregion.municipality_id
ORDER BY
  projects_municipality.muni_id ASC






COPY FROM OLD, COPY TO NEW

COPY (SELECT municipality_id, project_id FROM projects_project_municipalities) TO '/home/ubuntu/tmp/mf_join_muni_project.csv' DELIMITER ',' CSV HEADER;
COPY (SELECT project_id, subregion_id FROM projects_project_subregions) TO '/home/ubuntu/tmp/mf_join_project_subregion.csv' DELIMITER ',' CSV HEADER;
COPY (SELECT municipality_id, subregion_id FROM projects_municipality_subregion) TO '/home/ubuntu/tmp/mf_join_muni_subregion.csv' DELIMITER ',' CSV HEADER;

COPY municipalities_projects FROM '/Users/mapcuser/Projects/MetroFuture In Action/in-action/db/fixtures/relations/mf_join_muni_project.csv' DELIMITER ',' CSV HEADER;
COPY projects_subregions FROM '/Users/mapcuser/Projects/MetroFuture In Action/in-action/db/fixtures/relations/mf_join_project_subregion.csv' DELIMITER ',' CSV HEADER;
COPY municipalities_subregions FROM '/Users/mapcuser/Projects/MetroFuture In Action/in-action/db/fixtures/relations/mf_join_muni_subregion.csv' DELIMITER ',' CSV HEADER;





TRYING TO TRANSFORM TO 4326

COPY (SELECT gid AS id, muni_id, municipal AS name, ST_AsText(ST_Transform(ST_SetSRID(geom, 26986), 4326)) AS geom FROM gisdata.subregions_simple) TO '/Users/mapcuser/Projects/Metrofuture In Action/in-action/db/fixtures/geometries/subregions/subregions.csv' DELIMITER ',' CSV HEADER;
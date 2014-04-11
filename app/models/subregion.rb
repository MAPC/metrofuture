class Subregion < ActiveRecord::Base
  attr_accessible :abbr, :geom, :name, :id, :muni_id

  has_and_belongs_to_many :municipalities

  GEOFACTORY = RGeo::Geographic.spherical_factory(srid: 4326)
  set_rgeo_factory_for_column(:geom, GEOFACTORY)

  validates :name, presence: true, length: { minimum: 3, maximum: 70 }
  validates :abbr, presence: true, length: { minimum: 2, maximum: 5 }
end
















# Projects joined to Municipality information

# SELECT
#   projects_municipality.muni_id,
#   projects_municipality.name,
#   projects_project_municipalities.project_id
# FROM
#   projects_municipality
# INNER JOIN
#   projects_project_municipalities ON projects_municipality.muni_id = projects_project_municipalities.municipality_id
# ORDER BY
#   projects_project_municipalities.project_id ASC


# Projects joined to Subregion information

# SELECT
#   projects_subregion.id AS subregion_id,
#   projects_subregion.name AS subregion_name,
#   projects_project_subregions.project_id
# FROM
#   projects_subregion
# INNER JOIN
#   projects_project_subregions ON projects_subregion.id = projects_project_subregions.subregion_id
# ORDER BY
#   projects_project_subregions.project_id ASC


# SELECT
#   projects_municipality.id,
#   projects_municipality.muni_id,
#   projects_municipality_subregion.municipality_id,
#   projects_municipality_subregion.subregion_id
# FROM
#   projects_municipality
# INNER JOIN
#   projects_municipality_subregion ON projects_municipality.muni_id = projects_municipality_subregion.municipality_id
# ORDER BY
#   projects_municipality.muni_id ASC

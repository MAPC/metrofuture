class Subregion < ActiveRecord::Base
  attr_accessible :abbr, :geom, :name

  has_and_belongs_to_many :municipalities

  GEOFACTORY = RGeo::Geographic.spherical_factory(srid: 4326)
  set_rgeo_factory_for_column(:geom, GEOFACTORY)

  validates :name, presence: true, length: { minimum: 3, maximum: 70 }
  validates :abbr, presence: true, length: { minimum: 2, maximum: 5 }
end
 
class Municipality < ActiveRecord::Base
  attr_accessible :muni_id, :name, :geom

  belongs_to :community_subtype
  has_and_belongs_to_many :subregions

  GEOFACTORY = RGeo::Geographic.spherical_factory(srid: 4326)
  set_rgeo_factory_for_column(:geom, GEOFACTORY)

  validates :name, presence: true, length: { minimum: 3, maximum: 70 }

  def community_type
    self.community_subtype.community_type
  end
end

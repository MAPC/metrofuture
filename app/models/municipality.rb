class Municipality < ActiveRecord::Base
  attr_accessible :muni_id, :name, :geom

  belongs_to :community_subtype
  has_and_belongs_to_many :subregions

  GEOFACTORY = RGeo::Geographic.spherical_factory(srid: 4326)
  set_rgeo_factory_for_column(:geom, GEOFACTORY)

  validates :name, presence: true, length: { minimum: 3, maximum: 70 }

  def community_type
    community_subtype.community_type unless community_subtype.nil?
  end

  def subregion_name
    subregions.pluck(:name).first || nil
  end
end

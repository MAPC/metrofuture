class CommunitySubtype < ActiveRecord::Base
  belongs_to :community_type
  attr_accessible :id, :abbr, :name, :community_type_id

  validates :name, presence: true, length: { minimum: 3, maximum: 70 }
  validates :abbr, presence: true, length: { minimum: 2, maximum: 5 }
end

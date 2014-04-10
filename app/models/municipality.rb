class Municipality < ActiveRecord::Base
  belongs_to :community_type
  attr_accessible :name
end

# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

require 'fixtures/community_types'
require 'fixtures/community_subtypes'
require 'fixtures/departments'
require 'fixtures/funding_sources'
require 'fixtures/strategies'
require 'fixtures/substrategies'

require 'fixtures/municipalities'
require 'fixtures/subregions'
require 'fixtures/regions'
require 'fixtures/counties'


models = %w( County ) # CommunityType CommunitySubtype Department FundingSource Municipality Strategy SubStrategy Subregion Region

models.each do |class_name|
  model = Module.const_get class_name
  model.destroy_all
  model.reset_pk_sequence
end


# CommunityType.create    community_types
# CommunitySubtype.create community_subtypes
# Department.create       departments
# FundingSource.create    funding_sources
# Strategy.create         strategies
# SubStrategy.create      substrategies

# Municipality.create     municipalities
# muni_subtypes

# Subregion.create        subregions
# Region.create           regions
County.create(counties, without_protection: true)
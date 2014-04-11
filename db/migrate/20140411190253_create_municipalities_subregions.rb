class CreateMunicipalitiesSubregions < ActiveRecord::Migration
  def change
    create_table :municipalities_subregions do |t|
      t.belongs_to :municipality
      t.belongs_to :subregion
    end
  end
end

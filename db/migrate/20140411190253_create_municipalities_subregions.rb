class CreateMunicipalitiesSubregions < ActiveRecord::Migration
  def change
    create_table :municipalities_subregions, id: false do |t|
      t.belongs_to :municipality
      t.belongs_to :subregion
    end
    add_index(:municipalities_subregions, [:municipality_id, :subregion_id], name: 'index_municipalities_subregions_on_muni_id_and_subregion_id')
  end
end
